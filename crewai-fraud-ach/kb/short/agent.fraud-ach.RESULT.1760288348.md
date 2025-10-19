```json
{
  "id": "db736c9753917a85",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288348,
  "host_pid": "9e6742732c60:1",
  "hash": "ea248e4efb936ae60049f6d8ae0ff8aa68214e8b0c229e8f510753fffee73778",
  "cid": "QmV1ea248e4efb936ae60049f6d8ae0ff8aa68214e8b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288348,
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
      "evaluated_at": 1760288348
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
  "sig": "4ade059ec98bf4b01ae3e37e29be1babe730bc34342af0643c7449a63e4f7880"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 28642320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}