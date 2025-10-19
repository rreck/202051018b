```json
{
  "id": "9419304347d7ac13",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294426,
  "host_pid": "9e6742732c60:1",
  "hash": "f673edb02a0c313493a921e175108c48e3a57cd79c6dcbcea7cb2e34f9e94e8f",
  "cid": "QmV1f673edb02a0c313493a921e175108c48e3a57cd7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294426,
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
      "evaluated_at": 1760294426
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
  "sig": "d0b8bf57c520efcec28521e079e34513bcf204d91b4222ffe4c32ddbfdb0cb7e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246372706
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 66784228, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'b5568fe52f6cf528'}}}