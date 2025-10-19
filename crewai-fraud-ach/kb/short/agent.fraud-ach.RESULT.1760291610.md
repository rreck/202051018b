```json
{
  "id": "990aa205b7a8ebc7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291610,
  "host_pid": "9e6742732c60:1",
  "hash": "72e65bd39aeac0ab94463bef6d2f05fcd834f1ffe446d6250ac2565c33d02ca1",
  "cid": "QmV172e65bd39aeac0ab94463bef6d2f05fcd834f1ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291610,
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
      "evaluated_at": 1760291610
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
  "sig": "93ebfd54082daf595edf8455b3f32b3d6a24ee1ac0317dfcc51537aa523d8640"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037758614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 14666544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': '8cf13377232eef82'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '020899456', 'validation_error': 'Invalid routing number checksum'}}}