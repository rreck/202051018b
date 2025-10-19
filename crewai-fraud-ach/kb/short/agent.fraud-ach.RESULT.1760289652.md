```json
{
  "id": "d1f6929e09687607",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289652,
  "host_pid": "9e6742732c60:1",
  "hash": "182fad590d8e305ef3bb839f823537ccf0b19680af36f9ece5370dad2e8518ea",
  "cid": "QmV1182fad590d8e305ef3bb839f823537ccf0b19680",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289652,
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
      "evaluated_at": 1760289652
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
  "sig": "ffead12aa4bb81cf6112543244820e107b5e35377b5ba8b68fe218a5232e34f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245381675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 21158709, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}