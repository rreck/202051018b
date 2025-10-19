```json
{
  "id": "4c76fb4a4fe6e262",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289817,
  "host_pid": "9e6742732c60:1",
  "hash": "dfef7dc001ea0dbc45252dfb02cb8515cfdad1f7660605f4d58c64fa57108f1b",
  "cid": "QmV1dfef7dc001ea0dbc45252dfb02cb8515cfdad1f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289817,
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
      "evaluated_at": 1760289817
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
  "sig": "1a18de1ad74d03b21e916d0a0920ba8365c7395de0234ca3e54acbe6a163056d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246611704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 39864196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': '524463c0aee194a0'}}}