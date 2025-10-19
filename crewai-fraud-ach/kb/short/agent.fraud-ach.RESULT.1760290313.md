```json
{
  "id": "75babdc47dad793d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290313,
  "host_pid": "9e6742732c60:1",
  "hash": "44acf61a3405e1f83fa719abdb13cafc0d4972e0db00cd8914d5b3a38827b2af",
  "cid": "QmV144acf61a3405e1f83fa719abdb13cafc0d4972e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290313,
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
      "evaluated_at": 1760290313
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
  "sig": "f1ce0038d0479b2f2ec70fffccdfd3e0607da00eb302f2bd9f5e4896cb4d3169"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026959997
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 33387963, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285764, 'matching_hash': '4bd6adbc5f3cfca3'}}}