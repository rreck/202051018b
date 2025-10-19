```json
{
  "id": "c2bd37bbce3bdc5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287463,
  "host_pid": "9e6742732c60:1",
  "hash": "4fd48d1a8dc736f3071e47734affa3ec623374f2b55123bd6810208ab0b650e6",
  "cid": "QmV14fd48d1a8dc736f3071e47734affa3ec623374f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287463,
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
      "evaluated_at": 1760287463
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "e0918de2677e007d2a2772623ca0df4c969bc3e9c08f4acd30884744d4a3ac73"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 044000031287652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 16901697, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285763, 'matching_hash': 'd2d8cdbc9df50106'}}}