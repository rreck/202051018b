```json
{
  "id": "62ccd42eacb38db1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290045,
  "host_pid": "9e6742732c60:1",
  "hash": "e8814713c5d9977ed8d844ada12d8d1cd05e8b651367c594522e15db8a4b7f53",
  "cid": "QmV1e8814713c5d9977ed8d844ada12d8d1cd05e8b65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290045,
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
      "evaluated_at": 1760290045
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
  "sig": "33ea780316d2b6932235c751632c7d643759bca304ee3c827ba94b81743bf656"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274960966
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 16346400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': 'f5e3b3cd48fefc81'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018325}}}