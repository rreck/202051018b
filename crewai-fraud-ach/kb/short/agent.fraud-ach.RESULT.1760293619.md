```json
{
  "id": "972cca6e0f8f5a01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293619,
  "host_pid": "9e6742732c60:1",
  "hash": "28911be0dc936cc8f39337119db0cb587cafc0a30a6a9fc8f68c007366dc4816",
  "cid": "QmV128911be0dc936cc8f39337119db0cb587cafc0a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293619,
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
      "evaluated_at": 1760293619
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
  "sig": "2199f0978b20e2a68129e2b6311f66a0c810c6673767dd8ab8ffa6400fdfce32"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248764263
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 80629956, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '9f14c95be52dc67f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}