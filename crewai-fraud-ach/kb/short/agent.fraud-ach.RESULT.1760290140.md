```json
{
  "id": "fd0fd3c5ffeb2d1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290140,
  "host_pid": "9e6742732c60:1",
  "hash": "a298a2b0dab0d75d5d7f0c70034e0f43dc8186821ffd96be00477a920b7ecee9",
  "cid": "QmV1a298a2b0dab0d75d5d7f0c70034e0f43dc818682",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290140,
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
      "evaluated_at": 1760290140
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
  "sig": "d978579e2f5e474347c8a400ecb091b30267c64566dd67485ec49559fbfdb969"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 45191216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}