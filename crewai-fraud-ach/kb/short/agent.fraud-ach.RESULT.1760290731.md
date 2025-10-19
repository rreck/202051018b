```json
{
  "id": "5d3c237e552069c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290731,
  "host_pid": "9e6742732c60:1",
  "hash": "7ce3a8f9ef7813bb6ff185db4a63434802a7c84a1b6eeaafb9d7f5f0b3f3e115",
  "cid": "QmV17ce3a8f9ef7813bb6ff185db4a63434802a7c84a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290731,
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
      "evaluated_at": 1760290731
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
  "sig": "d1ce9b6a6da4555f572b56996985f97125c7127cef9c74fef84751078c4046c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270864889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 30037222, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': 'c03eacc7eaf45e0d'}}}