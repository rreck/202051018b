```json
{
  "id": "ad4117799a4e2fc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289673,
  "host_pid": "9e6742732c60:1",
  "hash": "c0cbb47b42750dba43ceecb423860b20e7e6a48c6fa8c38c3c690760e816b141",
  "cid": "QmV1c0cbb47b42750dba43ceecb423860b20e7e6a48c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289673,
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
      "evaluated_at": 1760289673
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
  "sig": "33b24a2ba23d84d1e021d7593e3356347a538fcf59278d66c5e0d183f540b5bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034886670
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 17787250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': 'cbf6d0e6528ee173'}}}