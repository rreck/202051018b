```json
{
  "id": "79a4056d14f24c36",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287071,
  "host_pid": "9e6742732c60:1",
  "hash": "635905a7866940b575ebbfb9a22abbc79d62fdc72a381809f83a5f259d9c176b",
  "cid": "QmV1635905a7866940b575ebbfb9a22abbc79d62fdc7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287071,
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
      "evaluated_at": 1760287071
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
  "sig": "41dade494c34c94af33c74cc9cd691fce919cc5948379b32c2adbdfc0d92a36d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105157447901
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}