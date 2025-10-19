```json
{
  "id": "dd478db99e274b48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292471,
  "host_pid": "9e6742732c60:1",
  "hash": "6aba3beca13882822a6016c0db0fb1ad7702dc79514776499d81947145a43421",
  "cid": "QmV16aba3beca13882822a6016c0db0fb1ad7702dc79",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292471,
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
      "evaluated_at": 1760292471
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
  "sig": "f7e19930f956b26e408e0095b68fcb67e36f61b154d0c586ea2f16d1d4328ed2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022074928
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': 'a87d8bfbdd334181'}}}een': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}