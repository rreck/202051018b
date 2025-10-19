```json
{
  "id": "c8d8642314014c22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294410,
  "host_pid": "9e6742732c60:1",
  "hash": "cd6cb87e0afdeb6be782d42862a99461f258de41085b21c09d797846dfb8469a",
  "cid": "QmV1cd6cb87e0afdeb6be782d42862a99461f258de41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294410,
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
      "evaluated_at": 1760294410
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
  "sig": "35efb72bda9e27c967215927417b2ac1d9690d367a5893bc53600cbd2b5318dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 22467363, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}