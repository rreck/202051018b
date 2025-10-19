```json
{
  "id": "a89b0672e82806f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291071,
  "host_pid": "9e6742732c60:1",
  "hash": "bc008929c2ac6ea27a439e528375ca8d355f31e87fe88b281e249e5e99759fd5",
  "cid": "QmV1bc008929c2ac6ea27a439e528375ca8d355f31e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291071,
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
      "evaluated_at": 1760291071
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
  "sig": "177b1f353454d60218508a10db50f4fc415bad88e466ecfc39f625cedf0b7fb7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598500621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 59198256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': '36e427bddf577026'}}}