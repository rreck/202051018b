```json
{
  "id": "313a91e5165d714e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288141,
  "host_pid": "9e6742732c60:1",
  "hash": "eb069341b90f425806f90ff250e44ede8bd56a1da49723e22f4aace0d0de8b80",
  "cid": "QmV1eb069341b90f425806f90ff250e44ede8bd56a1d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288141,
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
      "evaluated_at": 1760288141
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
  "sig": "e6ab2a0696262f0fc024054c7bacdf527b4812c75ef35927a1dcdba78b2aa442"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027679172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 36477672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': 'bcf2a51730a73925'}}}