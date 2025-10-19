```json
{
  "id": "3db240412579c72d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289328,
  "host_pid": "9e6742732c60:1",
  "hash": "e8add8a0118d2bf2ef943acadb22201659e052cd71ec9ff966dcf041cd5ae2ea",
  "cid": "QmV1e8add8a0118d2bf2ef943acadb22201659e052cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289328,
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
      "evaluated_at": 1760289328
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
  "sig": "e48c894e4f4e70ae93cc68fb5ab718c149ebbf323d190f22cd88a94b666625f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243741176
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 36517800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': 'e78a513bf0bcec2f'}}}