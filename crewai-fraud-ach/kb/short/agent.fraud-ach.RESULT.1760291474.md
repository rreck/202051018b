```json
{
  "id": "c0b0a11b4a8f4ff8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291474,
  "host_pid": "9e6742732c60:1",
  "hash": "97eef029b53af7060a99fed319e4a49404db2ce1aa568d677dc7d56831141753",
  "cid": "QmV197eef029b53af7060a99fed319e4a49404db2ce1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291474,
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
      "evaluated_at": 1760291474
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
  "sig": "1914ab5b8c782e29b24f255d111a0f81b28b543cb4863c4a4eb869b1fd88cbe6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020009015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 81797936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': 'f404409c8af40265'}}}