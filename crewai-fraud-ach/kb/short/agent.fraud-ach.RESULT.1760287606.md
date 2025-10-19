```json
{
  "id": "0c87b3d29d1140f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287606,
  "host_pid": "9e6742732c60:1",
  "hash": "3adb91e8092317d8d804c72990564c82224e3393fbe1ad207abf35d9055542e6",
  "cid": "QmV13adb91e8092317d8d804c72990564c82224e3393",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287606,
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
      "evaluated_at": 1760287606
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
  "sig": "44bf1c4a04cfbac1d6e9b1123967106eedf959f88ba4015480e6bff253d4ea49"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 111000025341279
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 27148770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285763, 'matching_hash': 'e2ff1695635a899d'}}}