```json
{
  "id": "a7d015c261c2dc0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289765,
  "host_pid": "9e6742732c60:1",
  "hash": "e211302a95528b94f47cc67a3474fe3a700e9170ba093d463367d36a6060f0cd",
  "cid": "QmV1e211302a95528b94f47cc67a3474fe3a700e9170",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289765,
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
      "evaluated_at": 1760289765
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
  "sig": "0a00c1f03c1e260f1fe2f5b77778360a149739d995d4caa3358a9836bf9a54a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467798287
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 58646676, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285765, 'matching_hash': 'b1c6e5e3cdd02671'}}}