```json
{
  "id": "86bb2521b5a4b4f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292230,
  "host_pid": "9e6742732c60:1",
  "hash": "00b05600ee9d15b4018d4ec04dfbb56965a27bf993fa9d3d429eddf67c09498f",
  "cid": "QmV100b05600ee9d15b4018d4ec04dfbb56965a27bf9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292230,
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
      "evaluated_at": 1760292230
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
  "sig": "859747a512b50bb4834ecdcd3ca0016ee5de25914542a6656b239c68d19de33c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153135421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 73655748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '4394c86a949e27d6'}}}