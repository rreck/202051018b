```json
{
  "id": "dcbd678d97c21d8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293070,
  "host_pid": "9e6742732c60:1",
  "hash": "cfe9b6efa193e65f555f2e0e80405e46f0ce296a0e0100fdb2c624a064bf6315",
  "cid": "QmV1cfe9b6efa193e65f555f2e0e80405e46f0ce296a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293070,
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
      "evaluated_at": 1760293070
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
  "sig": "fc3a9f03481481874a370f80341c181e66542d1d00107d242ac11b6be00e376b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039250274
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 23951665, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': 'd24fc6d094fa29d9'}}}