```json
{
  "id": "1834b6a8a48e0e70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290506,
  "host_pid": "9e6742732c60:1",
  "hash": "01b21f79e7bb8dabbc5c8176a664064bc3eef639eb7db4878d3b869607d2bcbf",
  "cid": "QmV101b21f79e7bb8dabbc5c8176a664064bc3eef639",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290506,
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
      "evaluated_at": 1760290506
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
  "sig": "107acf15cefd43408276b84aaae310e42231ea97bc483daf1b5701b3b183cb29"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242903308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 21512104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285764, 'matching_hash': '3fe1582345d32257'}}}