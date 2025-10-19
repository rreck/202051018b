```json
{
  "id": "719dab571238c004",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291437,
  "host_pid": "9e6742732c60:1",
  "hash": "2413b2324121c5a693e384670291ce0eed2eb7a98418db64c342062c29c6b265",
  "cid": "QmV12413b2324121c5a693e384670291ce0eed2eb7a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291437,
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
      "evaluated_at": 1760291437
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
  "sig": "a703151822c1cbb0e00b87568084634c219a9a8b3bac1e743b34d86a728c1047"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029122182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 17500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '6eeeaf20a2fbd10d'}}}