```json
{
  "id": "fb830530ec897348",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293621,
  "host_pid": "9e6742732c60:1",
  "hash": "f08aeb0888520f1c2c4172eed3649b33af4825353556d40586d0012c95c0980f",
  "cid": "QmV1f08aeb0888520f1c2c4172eed3649b33af482535",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293621,
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
      "evaluated_at": 1760293622
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
  "sig": "10636086274380cb6f8d5dd3d1afee2756004091b757eed17a463c848c2e1936"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245017605
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 104434572, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}