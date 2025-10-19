```json
{
  "id": "c8d9a3fc42b8f836",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289138,
  "host_pid": "9e6742732c60:1",
  "hash": "4af903944b2134b5dcd59d3d47c08c981066743d2bb6d3a10aecba669372b60f",
  "cid": "QmV14af903944b2134b5dcd59d3d47c08c981066743d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289138,
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
      "evaluated_at": 1760289138
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
  "sig": "fcd422a39856511ed22ea0a870a8aeae6fe02cbb0c4ef1a82242537b4d09be96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 36280272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}