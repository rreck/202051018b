```json
{
  "id": "ffdda78aeffa936c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289092,
  "host_pid": "9e6742732c60:1",
  "hash": "664d94aece07d678045d9a914c25be2e7b43ea8100f5264e6257530d83568886",
  "cid": "QmV1664d94aece07d678045d9a914c25be2e7b43ea81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289092,
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
      "evaluated_at": 1760289092
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
  "sig": "393f8cad439dc41071e28ff45d3ddfc93c7831ee2e1129b10e78ab96188973d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025262531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 36000670, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': 'cd477724f7ce5ce7'}}}