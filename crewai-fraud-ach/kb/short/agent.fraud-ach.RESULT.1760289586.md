```json
{
  "id": "d0e7c74613ab809d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289586,
  "host_pid": "9e6742732c60:1",
  "hash": "132e1675c012557043b3c3fa368f031a9d572634fde566379a8648e78745f84d",
  "cid": "QmV1132e1675c012557043b3c3fa368f031a9d572634",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289586,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760289586
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "1863fe46f72a601fc5ac557e0ffe0e34b8dc31f4ad6f2a496537a10db02337bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 35130359, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': 'a63e704272eccc25'}}}