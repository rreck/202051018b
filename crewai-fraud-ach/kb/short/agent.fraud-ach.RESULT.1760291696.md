```json
{
  "id": "ad1b29d7e2816486",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291696,
  "host_pid": "9e6742732c60:1",
  "hash": "7af888fd1cf364b71fe3528da1a573f6223281e3f34ee29e746081343b891def",
  "cid": "QmV17af888fd1cf364b71fe3528da1a573f6223281e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291696,
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
      "evaluated_at": 1760291696
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
  "sig": "8faae1899c70f3acddac6285e108edf8108279609c41dbb1119d1a2963bb21f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243661505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 75651846, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285764, 'matching_hash': '37851bbce8ea73db'}}}