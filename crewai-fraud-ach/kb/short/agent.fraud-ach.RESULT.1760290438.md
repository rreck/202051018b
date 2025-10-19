```json
{
  "id": "992355c3d41fce3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290438,
  "host_pid": "9e6742732c60:1",
  "hash": "d7a8267b03ec81b40a8bf4fc47f375021a5d003aae6db6ec134d24c72ae79bf4",
  "cid": "QmV1d7a8267b03ec81b40a8bf4fc47f375021a5d003a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290438,
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
      "evaluated_at": 1760290438
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
  "sig": "482f6cda13d95d4f126a8e411efb73fe0d4993026de147acf6919ec798b54329"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032270621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 34609200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285764, 'matching_hash': '380f2fccd8369f51'}}}