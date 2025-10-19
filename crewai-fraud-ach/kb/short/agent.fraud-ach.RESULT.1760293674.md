```json
{
  "id": "7952e80ec6792e76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293674,
  "host_pid": "9e6742732c60:1",
  "hash": "8f5a4b23291f6aefebb8db0ea30392493c8ca4109a00310d14f800c6e3be0ada",
  "cid": "QmV18f5a4b23291f6aefebb8db0ea30392493c8ca410",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293674,
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
      "evaluated_at": 1760293674
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
  "sig": "7d436eb5bfd42913544fa2b2bc1ec66eeeba2e66099fad6bd25f604876ab02d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594679703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 20453114, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285765, 'matching_hash': 'e094f64527cf9b58'}}}