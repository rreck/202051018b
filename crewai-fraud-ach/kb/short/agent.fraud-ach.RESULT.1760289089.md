```json
{
  "id": "4725598bb22fa293",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289089,
  "host_pid": "9e6742732c60:1",
  "hash": "d6e0ddd38d4f20c0950daa132195585f6f9297e27cbf12a14cd5c9c06315fbe5",
  "cid": "QmV1d6e0ddd38d4f20c0950daa132195585f6f9297e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289089,
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
      "evaluated_at": 1760289089
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
  "sig": "550faafe688dd2b3e67421d419e831e64b94e0527b80d92e8708558c363caea0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152435370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 18117968, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': '79f1dacfe7837a08'}}}