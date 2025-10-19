```json
{
  "id": "9c16313309861260",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291962,
  "host_pid": "9e6742732c60:1",
  "hash": "c02c891630bce9151d556d6556d2c4a131b134cf9c9f079545825a4cff9afc5a",
  "cid": "QmV1c02c891630bce9151d556d6556d2c4a131b134cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291962,
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
      "evaluated_at": 1760291962
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
  "sig": "68b496ea156ad21ca3b6be05976c6541a30c35a9d2674bf46c6584a75de92036"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 122105152842303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 93500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285764, 'matching_hash': 'f130ef58b190a1ab'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}