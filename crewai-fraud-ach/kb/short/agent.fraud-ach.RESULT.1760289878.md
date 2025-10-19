```json
{
  "id": "0da89e1062cf01af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289878,
  "host_pid": "9e6742732c60:1",
  "hash": "690782f5e7cec75f65a897d1a944d03d1ec9fdf57b6cbaf1fed2c44e5a2cbfa5",
  "cid": "QmV1690782f5e7cec75f65a897d1a944d03d1ec9fdf5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289878,
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
      "evaluated_at": 1760289878
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
  "sig": "447a19354cd9300c9d5e4951b28ab6fc64a42471729a58da8106a9606cd2da5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245511773
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 26065125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': '976242956abb43a6'}}}