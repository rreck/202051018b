```json
{
  "id": "934421f8a1a63e30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293355,
  "host_pid": "9e6742732c60:1",
  "hash": "c52e30081e68ff1485e3b5fd225297d00bd682d8c11100321878eaf8be844787",
  "cid": "QmV1c52e30081e68ff1485e3b5fd225297d00bd682d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293355,
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
      "evaluated_at": 1760293355
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
  "sig": "b9c45dc91a676228ce8740da4dea3abccb9c332c53c22f965792bf34320ff4f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596004100
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 34464157, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '0723803785cdf871'}}}