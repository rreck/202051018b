```json
{
  "id": "bc3c18ff94c4e689",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286711,
  "host_pid": "9e6742732c60:1",
  "hash": "cce1724450c85bf1305fa1ef34a680df5fb7623d17a49b21c08c20d118cf674f",
  "cid": "QmV1cce1724450c85bf1305fa1ef34a680df5fb7623d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286711,
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
      "evaluated_at": 1760286711
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
  "sig": "c8a5979bca310861b067a8a7b73b77bfd3576785c18b0366b719a89a1426b03e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10820432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}