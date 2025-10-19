```json
{
  "id": "a80a46dd0e306212",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289941,
  "host_pid": "9e6742732c60:1",
  "hash": "f8a1bfe3f1d51c1403a6473ed9e328b0deb6fb2143c3796b869c16d303c1ca21",
  "cid": "QmV1f8a1bfe3f1d51c1403a6473ed9e328b0deb6fb21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289941,
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
      "evaluated_at": 1760289942
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
  "sig": "96fea64f45343aa91346da3709323395207ebae474062722bbac1907e44806d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034789126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 45594993, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760284979, 'matching_hash': '5ec025bcbfaa0fd9'}}}