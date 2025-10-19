```json
{
  "id": "0f28d1883ed82550",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290213,
  "host_pid": "9e6742732c60:1",
  "hash": "44f64062cd2f88833fbe5d0199ea770db085ad46503132513fbde6c54d48631c",
  "cid": "QmV144f64062cd2f88833fbe5d0199ea770db085ad46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290213,
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
      "evaluated_at": 1760290213
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
  "sig": "b43bd95b82d513e6607241d963c4a2f533de741bf0b306965e3cb2fc4a87b90c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159928324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 63315792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': 'f9e49b53b0020755'}}}