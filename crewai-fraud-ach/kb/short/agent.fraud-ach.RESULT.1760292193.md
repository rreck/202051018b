```json
{
  "id": "b3834fb19eb59040",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292193,
  "host_pid": "9e6742732c60:1",
  "hash": "b04a50018d3a39503cb793e191a22d215112aff24d265d244b33cec17dcdd4f3",
  "cid": "QmV1b04a50018d3a39503cb793e191a22d215112aff2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292193,
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
      "evaluated_at": 1760292194
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
  "sig": "73ccd3a4325ef4ef71c57349b0b09b176ada802601fd0b70e6078e82d6abfe4e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152187504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 90709248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '4c6bc703d31ba532'}}}