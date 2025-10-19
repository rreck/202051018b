```json
{
  "id": "021a1f6d89caa04d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291433,
  "host_pid": "9e6742732c60:1",
  "hash": "6cdae648bd3b18a2c035b011feef1f90a1128cc353fcd69b44bbe1aed38cea70",
  "cid": "QmV16cdae648bd3b18a2c035b011feef1f90a1128cc3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291433,
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
      "evaluated_at": 1760291433
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
  "sig": "990be6aa19ee8b786b4f0023ff113dd15274d45ff40bb1bd84d717dfa51a335d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272419137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 45234350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '38281b9a763b4bf2'}}}