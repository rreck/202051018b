```json
{
  "id": "f7d31b8e643ea7b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294344,
  "host_pid": "9e6742732c60:1",
  "hash": "1520edf3cc2a99348404bbbd92c0589f2ec50acbb54eb02a6c20368910f80052",
  "cid": "QmV11520edf3cc2a99348404bbbd92c0589f2ec50acb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294344,
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
      "evaluated_at": 1760294344
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
  "sig": "dff8cad7d88dd21e1e3ac9741b37c93afe29a22a6a95f49737f0e60cc5f3b9b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023924602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 94978908, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285764, 'matching_hash': '8a38ff5636f784bb'}}}}