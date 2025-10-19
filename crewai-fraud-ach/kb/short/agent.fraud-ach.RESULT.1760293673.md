```json
{
  "id": "867f7aa09ef1aab1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293673,
  "host_pid": "9e6742732c60:1",
  "hash": "1ac88783b0f87876b6d49849aec46d8222e3725065d373f686a2ecfb8d6b9c8d",
  "cid": "QmV11ac88783b0f87876b6d49849aec46d8222e37250",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293673,
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
      "evaluated_at": 1760293673
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
  "sig": "0d23e32d02765588481398abd23589d29c9892a0d6a297f65c16631a22f863de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026184073
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 69625283, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '5c433365b4c36f89'}}}