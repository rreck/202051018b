```json
{
  "id": "60098ade81861d93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294338,
  "host_pid": "9e6742732c60:1",
  "hash": "25561cdfbc7afecf2bb1ad8cfa71d3ea539d8025376551a02393088e96b69e01",
  "cid": "QmV125561cdfbc7afecf2bb1ad8cfa71d3ea539d8025",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294338,
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
      "evaluated_at": 1760294339
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
  "sig": "c7147d84442661ff89259e5cbf13cbc1d81a3f7d9533e40b31911c46cefc327b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596636125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 105086552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'de29ac64387e8e3f'}}}