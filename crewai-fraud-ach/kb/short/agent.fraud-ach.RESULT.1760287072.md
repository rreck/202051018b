```json
{
  "id": "47f2ea5ec387ba00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287072,
  "host_pid": "9e6742732c60:1",
  "hash": "490ec20e3a8c7f7cdfbb7a5094c888be28c92a5046172d35ca518ab6b10e152f",
  "cid": "QmV1490ec20e3a8c7f7cdfbb7a5094c888be28c92a50",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287072,
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
      "evaluated_at": 1760287072
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "5026fafb6b197497833c9bd6d18715506ee38ef495e878a988e61236ba97e7e9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462119178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 19903513, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285763, 'matching_hash': '2f807700ebd65d7c'}}}