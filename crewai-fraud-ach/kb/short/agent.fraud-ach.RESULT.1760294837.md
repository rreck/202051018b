```json
{
  "id": "7291eedda9514f4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294837,
  "host_pid": "9e6742732c60:1",
  "hash": "169f4f49b88837b670e75f4351c8f0707b49779296fcc3c4e6c6a41dbd5b6402",
  "cid": "QmV1169f4f49b88837b670e75f4351c8f0707b497792",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294837,
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
      "evaluated_at": 1760294837
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
  "sig": "cf4ecd28f539c77254889507d5201f84ddad695ef850d8b694829a61da8b4f86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593077739
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 66992800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'dc5b0e0c6a053908'}}}