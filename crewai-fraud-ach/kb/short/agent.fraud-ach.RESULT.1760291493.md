```json
{
  "id": "4179f80394253235",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291493,
  "host_pid": "9e6742732c60:1",
  "hash": "56a6cec1ea8c52cf14ee8bae8a46e7de3cde0e2393f752d0e24276e257896280",
  "cid": "QmV156a6cec1ea8c52cf14ee8bae8a46e7de3cde0e23",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291493,
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
      "evaluated_at": 1760291493
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
  "sig": "572a9c14367ca4da15975409c156f9d8e72b6dc6d655dc5ce4d27179ab592d22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598219019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 20099728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': '253a69ee76b5426a'}}}