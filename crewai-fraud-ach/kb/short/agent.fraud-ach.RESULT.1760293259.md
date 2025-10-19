```json
{
  "id": "418c72b450b8fe99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293259,
  "host_pid": "9e6742732c60:1",
  "hash": "cc324e28d3c026c6f05da15ef9d04aab83e4821fbd9c774636189a2ff4c4ae47",
  "cid": "QmV1cc324e28d3c026c6f05da15ef9d04aab83e4821f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293259,
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
      "evaluated_at": 1760293259
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
  "sig": "ae1ceb2c511fd50bdcf3b9755e3f9c9581322d38e3dc4f7383f198924d5de465"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462461467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 79485715, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '257546013422e30a'}}}