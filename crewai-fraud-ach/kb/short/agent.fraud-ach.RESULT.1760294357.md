```json
{
  "id": "da0caba3f499c89a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294357,
  "host_pid": "9e6742732c60:1",
  "hash": "be191f38cdb3eb7a16b0aa127d68eeb9ae44afd11cd17dd01f5936ef36acacdd",
  "cid": "QmV1be191f38cdb3eb7a16b0aa127d68eeb9ae44afd1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294357,
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
      "evaluated_at": 1760294357
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
  "sig": "d2aea202d9f45b222e77d6ae0ff5291ff8d8d29e6b96fef6af84b91ce7228ee7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031078531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 18149108, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}