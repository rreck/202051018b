```json
{
  "id": "36f3e7dcce0790b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288685,
  "host_pid": "9e6742732c60:1",
  "hash": "ac3bc8513f2b820c0f8f1971855fe883f8bd2fbaa97faaec5a5a807fbf02b20b",
  "cid": "QmV1ac3bc8513f2b820c0f8f1971855fe883f8bd2fba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288685,
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
      "evaluated_at": 1760288685
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
  "sig": "a75074199ed2ae0002947a22243ab3c3baa71c1f4ee2c51d022c41dae1eb4111"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 38522006, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}