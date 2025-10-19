```json
{
  "id": "1747c272444f35bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290701,
  "host_pid": "9e6742732c60:1",
  "hash": "1f782c3420fe94b27b0cbb7e85a6fa2dc61a82d907794b85f62b50bb5952759e",
  "cid": "QmV11f782c3420fe94b27b0cbb7e85a6fa2dc61a82d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290701,
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
      "evaluated_at": 1760290701
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
  "sig": "d6dcd67ac1339b4e794a96da52b2ace8fd9721c402afe60b161b75a4504baea2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460007503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 27957147, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '17a9441d6a1d37be'}}}maly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8435125}}}