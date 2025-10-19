```json
{
  "id": "622685083c05f455",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292502,
  "host_pid": "9e6742732c60:1",
  "hash": "590b99268a4bc87a77cabe6489cf2ad7053ecc5e17f6eca24ecc3fc1cbb985ce",
  "cid": "QmV1590b99268a4bc87a77cabe6489cf2ad7053ecc5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292502,
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
      "evaluated_at": 1760292502
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
  "sig": "d9ce1827dda946dc7f77d4e672a8208317f13dda45282383eb9797d78db8f912"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025319716
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 50886489, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': '46cae66c8ff70b91'}}}