```json
{
  "id": "646b49a1663b4ecb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294242,
  "host_pid": "9e6742732c60:1",
  "hash": "5a9f116bfb4adce6706fafec5a9301b20cc09438a998176a7696a5b5d6376e53",
  "cid": "QmV15a9f116bfb4adce6706fafec5a9301b20cc09438",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294242,
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
      "evaluated_at": 1760294242
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
  "sig": "e40a3b22448fc7096ae45fb528797d505ee68cdc8ccb6a7840282c34d1b53849"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273334011
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 24313536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': 'fc8e9fbdacff3816'}}}