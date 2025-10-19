```json
{
  "id": "2ee7a68b9443da2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288313,
  "host_pid": "9e6742732c60:1",
  "hash": "6c718a74dbd71bef29a617bd0bfb2af8dbe7b1adfed1e8937f61e3d0647834e7",
  "cid": "QmV16c718a74dbd71bef29a617bd0bfb2af8dbe7b1ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288313,
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
      "evaluated_at": 1760288313
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "f0bcf2499c11b70cca862df2313f39a511e4e340c5838c165dcb4b8347296f63"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201465841026
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 44500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285765, 'matching_hash': 'e2a83dab91a99cc0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}